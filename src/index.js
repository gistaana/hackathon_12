import "./css/reset.css";
import "./css/styles.css";
import { addData } from "./js/db_actions";

const email = document.querySelector("#email");
const name = document.querySelector("#name");
const form = document.querySelector("#form-main");
const actionStatusBox = document.querySelector("#action-status-pane");

function updateActionStatusBox(isError, email) {
    const messageBody = `added ${email} to our list`;
    const messageStart = isError ? "Unsuccessfully" : "Successfully";
    const messageEnd = isError ? ":(" : ":)";

    const message = `${messageStart} ${messageBody} ${messageEnd}`;

    actionStatusBox.classList.remove("db-error");
    actionStatusBox.classList.remove("db-success");

    const classToAdd = isError ? "db-error" : "db-success";

    actionStatusBox.classList.add(classToAdd);
    actionStatusBox.textContent = message;
}

form.addEventListener("submit", async (evt) => {
    evt.preventDefault(); // stop page refresh

    const userEmail = email.value;
    const userName = name.value;

    let isError = false;

    try {
        await addData(userEmail, userName);
        console.log(`added email=${userEmail} username=${userName}`);
    } catch (error) {
        console.log(error);
        isError = true;
    }

    updateActionStatusBox(isError, userEmail);
});
