import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: process.env.FIREBASE_apiKey,
    authDomain: process.env.FIREBASE_authDomain,
    projectId: process.env.FIREBASE_projectId,
    storageBucket: process.env.FIREBASE_storageBucket,
    messagingSenderId: process.env.FIREBASE_messagingSenderId,
    appId: process.env.FIREBASE_appId,
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);

export default app;
