const form = document.querySelector("#form");
const website = form.querySelector("#website");
const email = form.querySelector("#email");
const password = form.querySelector("#password");
const search = form.querySelector("#search");
const generatePassword = form.querySelector(`#generate`);

form.addEventListener("submit", (e) => {
    e.preventDefault();

    let userDetails = {
        website: website.value,
        email: email.value,
        password: password.value,
    };

    let options = {
        method: "POST",
        header: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(userDetails),
    };
    //end-point to submit the data
    fetch("/submit", options).then(res => res.json()).then(res => console.log(res)).catch(e => console.log(e));
});

search.addEventListener(`click`, (e) => {
    if (website.value.length === 0) {
        return;
    }

    let options = {
        method: "POST",
        body: JSON.stringify({ url: website.value })
    };
    fetch("/search", options).then(res => res.json()).then(res => res).catch(e => console.log(e));
});

generatePassword.addEventListener("click", (e) => {
    if (website.value.length === 0 || email.value.length === 0) {
        return;
    }

    let userDetails = {
        website: website.value,
        email: email.value,
    };

    let options = {
        method: "POST",
        header: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(userDetails),
    };
    fetch("/generate", options).then(res => res.json).then(res => password.value = res).catch(e => console.log(e));
});