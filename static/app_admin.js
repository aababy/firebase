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
            publish('app')
        }

        function publish(name) {
            let app_name = document.getElementById('id_name').value
            $.get("/ajax/publish/", {'filename': name, 'appname': app_name}, function (ret) {
                let id_name = document.getElementById('id_name').value
                let json = JSON.stringify(ret)
                storageRef.child('data/' + id_name + '/' + name + '.json').putString(json).then(function (snapshot) {
                    if (name == 'app') {
                        publish('tag')
                    } else if (name == 'tag') {
                        publish('graph')
                    } else {
                        alert('publish succeed.')
                    }
                }).catch(function (error) {
                    alert('publish failed.')
                });
            })
        }
    }
})(django.jQuery);
