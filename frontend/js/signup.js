const form = document.querySelector('#signup-form');

const checkPassword = () => {
  const formData = new FormData(form);
  const pw1 = formData.get('password')
  const pw2 = formData.get('password2')
  if (pw1===pw2) {
    return true
  }else return false
}

const handleSubmitForm = async (event) => {
  event.preventDefault();
  const data = new FormData(form)
  const sha256Password = sha256(data.get('password'))
  data.set('password', sha256Password)
  const div =document.querySelector("#pw-info");
  if (checkPassword()){
    const res = await fetch('/signup',{
      method:"POST",
      body:data
    });
    const resJson = await res.json()
    if (resJson === "200"){
      alert('회원 가입에 성공했습니다.');
      window.location.pathname='/login.html';
    }
  }else {
    div.innerText ="비밀번호가 같지않습니다.";
    div.style.color = "red";
  }
  
};

form.addEventListener("submit",handleSubmitForm)