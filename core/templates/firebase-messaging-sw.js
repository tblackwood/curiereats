importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js");

firebase.initializeApp({
    apiKey: "AIzaSyB7Flkipb68FWgcTwZB7jr16UMJbQxzYbQ",
    authDomain: "curiereats.firebaseapp.com",
    projectId: "curiereats",
    storageBucket: "curiereats.appspot.com",
    messagingSenderId: "526444542314",
    appId: "1:526444542314:web:4a4958f42f6993ed438d13"
});

const messaging = firebase.messaging();