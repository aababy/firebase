(function ($) {
    window.onload = function () {
        //如果不是编辑界面，那么就不执行下面的操作
        if (window.location.pathname == '/admin/storage/app/') {
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

        $('#id_name').after('<input type="button" id="id_publish" class="button" name="publish" value="Publish"></input>') //插入按钮
        $('#id_publish').css("marginLeft", "8px")
        $('#id_publish').click(handlePublish);
        document.getElementById('id_publish').disabled = true;

        auth.onAuthStateChanged(function (user) {
            if (user) {               
                console.log('Anonymous user signed-in.', user);
                document.getElementById('id_publish').disabled = false;
            } else {
                console.log('There was no anonymous session. Creating a new anonymous user.');
                auth.signInAnonymously();
            }
        });

        function handlePublish(evt) {
            $.get("/ajax/publish/", {}, function (ret) {
                let json = JSON.stringify(ret)
                storageRef.child('app/data').putString(json).then(function (snapshot) {
                    alert('publish succeed.');
                    // $.get("/ajax/message/", { 'msg': 'publish_succeed.', 'path': window.location.pathname }, function (ret) { })
                }).catch(function (error) {
                    alert('publish failed.');
                });
            })
        }
    }
})(django.jQuery);
