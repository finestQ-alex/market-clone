import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
import { getStorage } from "firebase/storage";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  apiKey: "AIzaSyDn8ikADvWYDK5t9NUnEYOGwTIKxVpFfzE",
  authDomain: "carrot-market-886c1.firebaseapp.com",
  databaseURL:
    "https://carrot-market-886c1-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "carrot-market-886c1",
  storageBucket: "carrot-market-886c1.firebasestorage.app",
  messagingSenderId: "56297759130",
  appId: "1:56297759130:web:161a56b013883d5b50da23",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);
const storage = getStorage(app);
