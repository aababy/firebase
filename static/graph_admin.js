(function ($) {
    window.onload = function () {
        //如果不是编辑界面，那么就不执行下面的操作
        firebase.initializeApp(config);

        var auth = firebase.auth();
        var storageRef = firebase.storage().ref();

        if (window.location.pathname == '/storage/graph/') {
            var filesInfo = [];
            var notUploadInfo = [];
            var count = 0;
            var total = 0;
            showGraphs();
        } else {
            var graphs = null;
            $.get("/ajax/get_graphs/", {}, function (ret) {
                graphs = ret;
            })
            initGraph();
        }

        function showGraphs(params) {
            $('#content-main').after('<div id="my_container" class="flex"><input type="file" id="upload_file" name="file" multiple="multiple"/>' +
                '<label id="process"></label></div>')
            $('#upload_file').css('float', 'left')
            $('#upload_file').change(handleBatchSelect);
            document.getElementById('upload_file').disabled = true;

            auth.onAuthStateChanged(function (user) {
                if (user) {
                    console.log('Anonymous user signed-in.', user);
                    document.getElementById('upload_file').disabled = false;
                } else {
                    console.log('There was no anonymous session. Creating a new anonymous user.');
                    auth.signInAnonymously();
                }
            });
        }

        function initGraph() {
            $('#id_url').after('<input type="file" id="upload_file" name="file"/>') //插入按钮
            $('#upload_file').css("marginLeft", "8px")
            $('#upload_file').change(handleFileSelect);
            document.getElementById('upload_file').disabled = true;
    
            $('#id_original_url').after('<input type="file" id="upload_file_original" name="file"/>') //插入按钮
            $('#upload_file_original').css("marginLeft", "8px")
            $('#upload_file_original').change(handleFileSelectOriginal);
            document.getElementById('upload_file_original').disabled = true;

            auth.onAuthStateChanged(function (user) {
                if (user) {
                    console.log('Anonymous user signed-in.', user);
                    document.getElementById('upload_file').disabled = false;
                    document.getElementById('upload_file_original').disabled = false;
                } else {
                    console.log('There was no anonymous session. Creating a new anonymous user.');
                    auth.signInAnonymously();
                }
            });
        }

        function handleFileSelect(evt) {
            evt.stopPropagation();
            evt.preventDefault();
            var file = evt.target.files[0];
            var metadata = {
                'contentType': file.type
            };

            let dot = file.name.indexOf('_thumb.jpg');
            if (dot == -1) {
                alert('Your file name is wrong, it\'s suffix should be _thumb.jpg!');
                return;
            }

            //检查是否跟已有的graph重名
            if(document.getElementById('id_name').value != '' || checkFileName(file.name.slice(0, dot))) {
                document.getElementById('id_url').value = '';
                storageRef.child('jigsaw/graphs/' + file.name).put(file, metadata).then(function (snapshot) {
                    var url = snapshot.downloadURL;
                    let dot = file.name.indexOf('.');
                    let name = file.name.slice(0, dot);
    
                    let thumb = name.indexOf('_thumb');                 //fix thumb name
                    if (thumb != -1) {
                        name = name.slice(0, thumb);
                    }
                    
                    document.getElementById('id_name').value = name;
                    document.getElementById('id_url').value = url;    //$('#id_test1').val(url); //$('#id_test1')[0].value = url;
                }).catch(function (error) {
                    console.error('Upload failed:', error);
                    alert('Upload failed.')
                });
            } else {
                alert('Your file name is repeated with others!')
            }
        }

        function handleFileSelectOriginal(evt) {
            evt.stopPropagation();
            evt.preventDefault();
            var file = evt.target.files[0];
            var metadata = {
                'contentType': file.type
            };

            let dot = file.name.indexOf('.jpg');
            if (dot == -1) {
                alert('Your file name is wrong, it\'s suffix should be jpg!');
                return;
            }

            //检查是否跟已有的graph重名
            if(document.getElementById('id_name').value != '' || checkFileName(file.name.slice(0, dot))) {
                document.getElementById('id_original_url').value = '';
                storageRef.child('jigsaw/graphs/' + file.name).put(file, metadata).then(function (snapshot) {
                    var url = snapshot.downloadURL;
                    document.getElementById('id_original_url').value = url;    //$('#id_test1').val(url); //$('#id_test1')[0].value = url;
                }).catch(function (error) {
                    console.error('Upload failed:', error);
                    alert('Upload failed.')
                });
            } else {
                alert('Your file name is repeated with others!')
            }
        }

        function checkFileName(name) {
            for (let index = 0; index < graphs.length; index++) {
                const graph = graphs[index];
                if (graph.name == name) {
                    return false;
                }
            }
            return true;
        }

        class Info {
            constructor(name) {
                this.name = name;
                this.original = null;
                this.thumb = null;

                this.original_url = null;
                this.thumb_url = null;
            }

            isReady() {
                if (this.original_url != null && this.thumb_url != null) {
                    return true;
                } else {
                    return false;
                }
            }
        }

        function handleBatchSelect(evt) {
            evt.stopPropagation();
            evt.preventDefault();

            filesInfo = [];
            let files = evt.target.files;
            setFilesInfo(files);

            let names = [];
            for (let i = 0; i < filesInfo.length; i++) {
                names.push(filesInfo[i].name);
            }

            $.ajax({
                url: "/ajax/batch_check_graph/",
                type: "GET",
                data: {"data": names},
                traditional: true, 
                success: function(ret) {
                    if (ret.length == 0) {
                        uploadFiles();
                    } else {
                        let log = "";
                        for (let index = 0; index < ret.length; index++) {
                            log += ret[index] + " ";
                        }
                        log = 'The following file names are repeated with others : ' + log + ' Please do NOT upload them use batch.';
                        alert(log);
                    }
                }
            });
        }

        function uploadFiles() {
            notUploadInfo = [];
            count = 0;
            total = 0;

            for (let index = 0; index < filesInfo.length; index++) {
                const info = filesInfo[index];
                if (info.thumb != null && info.original != null) {
                    total += 2;
                } else {
                    notUploadInfo.push(filesInfo[index].name);
                }
            }

            let log = 'uploading: ' + count + '/' + total;
            $("#process").html(log);

            for (let index = 0; index < filesInfo.length; index++) {
                const info = filesInfo[index];
                if (info.thumb != null && info.original != null) {
                    uploadFile(info.name, info.thumb);
                    uploadFile(info.name, info.original);
                }
            }
        }

        function uploadFile(name, file) {
            var metadata = {
                'contentType': file.type
            };

            storageRef.child('jigsaw/graphs/' + file.name).put(file, metadata).then(function (snapshot) {
                count++;
                let log = 'uploading: ' + count + '/' + total;
                $("#process").html(log);

                let info = getFileInfo(name);
                if (file.name.indexOf('_thumb.jpg') != -1) {
                    info.thumb_url = snapshot.downloadURL;
                } else {
                    info.original_url = snapshot.downloadURL;
                }
                if (info.isReady()) {
                    //传数据给python
                    $.get("/ajax/batch_graphs/", {
                        'name': name,
                        'url': info.thumb_url,
                        'original_url': info.original_url,
                    }, function (ret) {
                        if (count >= total) {
                            log = "";
                            for (let i = 0; i < notUploadInfo.length; i++) {
                                log += notUploadInfo[i] + " ";
                            }

                            if (log.length == 0) {
                                log = 'Upload succeed.'
                            } else {
                                log = 'Upload succeed. The following has NOT been add: ' + log
                            }
                            alert(log);
                            $("#process").html("");
                            window.location.reload();
                        }
                    })
                }
            }).catch(function (error) {
                console.error('Upload failed:', error);
                alert('Upload failed.')
            });
        }

        function setFilesInfo(files) {
            for (let index = 0; index < files.length; index++) {
                let name = files[index].name;
                let dot = name.indexOf('_thumb.jpg');
                if (dot != -1) {
                    checkImageWidth(files[index], 512);
                    name = name.slice(0, dot);
                    let info = getFileInfo(name);
                    if (info == null) {
                        info = new Info(name);
                        filesInfo.push(info);
                    }
                    info.thumb = files[index];
                } else {
                    dot = name.indexOf('.jpg');
                    if (dot != -1) {
                        checkImageWidth(files[index], 2048);
                        name = name.slice(0, dot);
                        let info = getFileInfo(name);
                        if (info == null) {
                            info = new Info(name);
                            filesInfo.push(info);
                        }
                        info.original = files[index];
                    }
                }
            }
        }

        function getFileInfo(name) {
            for (let i = 0; i < filesInfo.length; i++) {
                const file = filesInfo[i];
                if (file.name == name) {
                    return file;
                }
            }
            return null;
        }

        function checkImageWidth(file, measure) {
            let filename = file.name
            //创建读取文件的对象  
            let reader = new FileReader();
            //为文件读取成功设置事件  
            reader.onload = function (e) {
                let data = e.target.result;
                //加载图片获取图片真实宽度和高度  
                let image = new Image();
                image.onload = function () {
                    let width = image.width;
                    let height = image.height;
                    if (width != measure || height != measure) {
                        alert(filename + ' is NOT ' + measure + ', please delete it and re upload!');
                    }
                };
                image.src = data;
            };

            //正式读取文件  
            reader.readAsDataURL(file);
        }
    }
})(django.jQuery);
