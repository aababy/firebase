(function ($) {
    window.onload = function () {
        //如果不是编辑界面，那么就不执行下面的操作
        if (window.location.pathname == '/admin/storage/app/') {
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
            document.getElementById('id_publish').disabled = true;
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
                        alert('Publish succeed.')
                    }
                }).catch(function (error) {
                    alert('Publish failed.')
                    document.getElementById('id_publish').disabled = false;
                });
            })
        }
    }
})(django.jQuery);
