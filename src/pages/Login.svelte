<script>
  import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
  import { user$ } from "../store";

  const provider = new GoogleAuthProvider();
  const auth = getAuth();

  const loginWithGoogle = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const credential = GoogleAuthProvider.credentialFromResult(result);
      const token = credential.accessToken;
      const user = result.user;
      user$.set(user);
      localStorage.setItem("token", token);
    } catch (error) {
      console.error(error);
    }
  };
</script>

<div>
  <div>로그인하기</div>
  <button class="login-btn" on:click={loginWithGoogle}>
    <img
      class="google-img"
      src="https://littledeep.com/wp-content/uploads/2019/03/google_logo_download_thumbnail.png"
      alt=""
    />
    <div>Google로 시작하기</div>
    <div></div>
  </button>
</div>

<style>
  .login-btn {
    width: 200px;
    height: 50px;
    display: flex;
    border: 1px solid gray;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    border-radius: 3px;
  }

  .google-img {
    width: 70px;
    margin-left: -20px;
    margin-right: -25px;
  }
</style>
