import { doc, setDoc } from "firebase/firestore";
import { db } from "../../firebase.config";

export function addData(email, name) {
    return setDoc(
        doc(db, process.env.FIREBASE_ROOT_COLLECTION_NAME, email),
        {
            email,
            name,
        },
        { merge: true }
    );
}
