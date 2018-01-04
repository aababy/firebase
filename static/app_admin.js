(function($) {
    var initialize = false;
    if (!initialize) {
        initialize = true;
        var config = {
            apiKey: "AIzaSyBvcx_zTTFWyOlkE8x1y1_I1bSl3zaFkrA",
            authDomain: "hidd-bigb001.firebaseapp.com",
            databaseURL: "https://hidd-bigb001.firebaseio.com",
            projectId: "hidd-bigb001",
            storageBucket: "hidd-bigb001.appspot.com",
            messagingSenderId: "278231656471"
        };
        firebase.initializeApp(config);
        console.log('initializeApp');
    }

    var auth = firebase.auth();
    var storageRef = firebase.storage().ref();
    console.log('storageRef:' + storageRef);

    function handlePublish(evt) {
        console.log('click');
    }

    window.onload = function() {
        // if (window.location.pathname != '/admin/polls/product/9/change/') {
        //   return;
        // } else 
        
        {
          let path = window.location.pathname;
          console.log(path);
          $('#id_name').after('<input type="button" id="id_publish" class="button" name="publish" value="Publish"></input>') //插入按钮
          $('#id_publish').css("marginLeft", "8px")
          $('#id_publish').click(handlePublish);
    
          auth.onAuthStateChanged(function(user) {
            if (user) {
              console.log('Anonymous user signed-in.', user);
              //document.getElementById('file').disabled = false;
            } else {
              console.log('There was no anonymous session. Creating a new anonymous user.');
              // Sign the user in anonymously since accessing Storage requires the user to be authorized.
              auth.signInAnonymously();
            }
          });
        }
      }
})(django.jQuery);
