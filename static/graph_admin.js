(function ($) {
    window.onload = function () {
        //如果不是编辑界面，那么就不执行下面的操作
        if (window.location.pathname == '/storage/graph/') {
            return;
        } else {
            var graphs = null;
            $.get("/ajax/get_graphs/", {}, function (ret) {
                graphs = ret;
            })
        }

        firebase.initializeApp(config);

        var auth = firebase.auth();
        var storageRef = firebase.storage().ref();

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
            if(checkFileName(file.name.slice(0, dot))) {
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
            if(checkFileName(file.name.slice(0, dot))) {
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
    }
})(django.jQuery);
