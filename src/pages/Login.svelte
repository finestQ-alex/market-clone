<form id="login-form" action="/signup" method="POST">
  <div>로그인하기</div>
  <div>
    <label for="id">아이디</label>
    <input type="text" name="id" id="id" required />
  </div>
  <div>
    <label for="password">패스워드</label>
    <input type="password" name="password" id="password" required />
  </div>
  <div>
    <button type="submit">로그인</button>
    <div id="info"></div>
  </div>
</form>
