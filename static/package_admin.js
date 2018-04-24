(function ($) {
    window.onload = function () {
        //如果不是编辑界面，那么就不执行下面的操作
        if (window.location.pathname == '/admin/storage/package/') {
            return;
        }

        //初始化
        var config = {
            apiKey: "AIzaSyAaKztuNaOumx941AHhWf11SCgXZMuAxyY",
            authDomain: "tobi-apps.firebaseapp.com",
            databaseURL: "https://tobi-apps.firebaseio.com",
            projectId: "tobi-apps",
            storageBucket: "tobi-apps.appspot.com",
            messagingSenderId: "405572885328"
        };
        firebase.initializeApp(config);

        var auth = firebase.auth();
        var storageRef = firebase.storage().ref();

        $('#id_url').after('<input type="file" id="upload_file" name="file"/>') //插入按钮
        $('#upload_file').css("marginLeft", "8px")
        $('#upload_file').change(handleFileSelect);
        document.getElementById('upload_file').disabled = true;

        $('#id_thumb_url').after('<input type="file" id="upload_file_thumb" name="file"/>') //插入按钮
        $('#upload_file_thumb').css("marginLeft", "8px")
        $('#upload_file_thumb').change(handleThumbFileSelect);
        document.getElementById('upload_file_thumb').disabled = true;

        auth.onAuthStateChanged(function (user) {
            if (user) {
                console.log('Anonymous user signed-in.', user);
                document.getElementById('upload_file').disabled = false;
                document.getElementById('upload_file_thumb').disabled = false;
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

            storageRef.child('jigsaw/packages/' + file.name).put(file, metadata).then(function (snapshot) {
                var url = snapshot.downloadURL;
                document.getElementById('id_name').value = file.name;
                document.getElementById('id_url').value = url;    //$('#id_test1').val(url); //$('#id_test1')[0].value = url;
            }).catch(function (error) {
                console.error('Upload failed:', error);
                alert('Upload failed.')
            });
        }

        function handleThumbFileSelect(evt) {
            evt.stopPropagation();
            evt.preventDefault();
            var file = evt.target.files[0];
            var metadata = {
                'contentType': file.type
            };

            storageRef.child('jigsaw/packages/' + file.name).put(file, metadata).then(function (snapshot) {
                var url = snapshot.downloadURL;
                document.getElementById('id_thumb_name').value = file.name;
                document.getElementById('id_thumb_url').value = url;    //$('#id_test1').val(url); //$('#id_test1')[0].value = url;
            }).catch(function (error) {
                console.error('Upload failed:', error);
                alert('Upload failed.')
            });
        }
    }
})(django.jQuery);
