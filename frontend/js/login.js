const form = document.querySelector('#login-form');


const handleSubmitForm = async (event) => {
  event.preventDefault();
  const data = new FormData(form)
  console.log(data)
  const sha256Password = sha256(data.get('password'))
  data.set('password', sha256Password)
  const res = await fetch('/login',{
    method:"POST",
    body:data
  });
  const resJson = await res.json()
  console.log(resJson)
  if (res.status === 200){
    window.localStorage.setItem("token", resJson.access_token)
    alert('로그인에 성공했습니다.');
    window.location.pathname='/';
  }else if (res.status === 401){
    alert('존재하지 않는 계정입니다.')
  }
}

form.addEventListener("submit",handleSubmitForm)