(function ($) {
    window.onload = function () {
        //如果不是编辑界面，那么就不执行下面的操作
        if (window.location.pathname == '/admin/storage/graph/') {
            return;
        }

        //初始化
        var config = {
            apiKey: "AIzaSyBvcx_zTTFWyOlkE8x1y1_I1bSl3zaFkrA",
            authDomain: "hidd-bigb001.firebaseapp.com",
            databaseURL: "https://hidd-bigb001.firebaseio.com",
            projectId: "hidd-bigb001",
            storageBucket: "hidd-bigb001.appspot.com",
            messagingSenderId: "278231656471"
        };
        firebase.initializeApp(config);

        var auth = firebase.auth();
        var storageRef = firebase.storage().ref();

        $('#id_url').after('<input type="file" id="upload_file" name="file"/>') //插入按钮
        $('#upload_file').css("marginLeft", "8px")
        $('#upload_file').change(handleFileSelect);
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

        function handleFileSelect(evt) {
            evt.stopPropagation();
            evt.preventDefault();
            var file = evt.target.files[0];
            var metadata = {
                'contentType': file.type
            };

            storageRef.child('graphs/' + file.name).put(file, metadata).then(function (snapshot) {
                var url = snapshot.downloadURL;
                console.log('File available at', url);
                let dot = file.name.indexOf('.');
                let name = file.name.slice(0, dot);
                document.getElementById('id_name').value = name;
                document.getElementById('id_url').value = url;    //$('#id_test1').val(url); //$('#id_test1')[0].value = url;
            }).catch(function (error) {
                console.error('Upload failed:', error);
            });
        }
    }
})(django.jQuery);
