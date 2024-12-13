<script>
  import { location } from "svelte-spa-router";
  const moveToHome = () => {
    window.location.hash = "/";
  };
  console.log(location);
</script>

<footer>
  <div class="footer-block">
    <button class="footer-icons" on:click={moveToHome}>
      <div class="footer-icons__img">
        {#if $location === "/"}
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="currentColor"
            class="size-6"
          >
            <path
              d="M11.47 3.841a.75.75 0 0 1 1.06 0l8.69 8.69a.75.75 0 1 0 1.06-1.061l-8.689-8.69a2.25 2.25 0 0 0-3.182 0l-8.69 8.69a.75.75 0 1 0 1.061 1.06l8.69-8.689Z"
            />
            <path
              d="m12 5.432 8.159 8.159c.03.03.06.058.091.086v6.198c0 1.035-.84 1.875-1.875 1.875H15a.75.75 0 0 1-.75-.75v-4.5a.75.75 0 0 0-.75-.75h-3a.75.75 0 0 0-.75.75V21a.75.75 0 0 1-.75.75H5.625a1.875 1.875 0 0 1-1.875-1.875v-6.198a2.29 2.29 0 0 0 .091-.086L12 5.432Z"
            />
          </svg>
        {:else}
          <img src="./assets/home-empty.svg" alt="" />
        {/if}
      </div>
      <div class="footer-icons__disc">홈</div>
    </button>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="./assets/newspaper-empty.svg" alt="" />
      </div>
      <div class="footer-icons__disc">동네생활</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="./assets/location-empty.svg" alt="" />
      </div>
      <div class="footer-icons__disc">내 근처</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="./assets/chat-empty.svg" alt="" />
      </div>
      <div class="footer-icons__disc">채팅</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="./assets/user-empty.svg" alt="" />
      </div>
      <div class="footer-icons__disc">나의 당근</div>
    </div>
  </div>
</footer>
