<script>
  import Main from "./pages/Main.svelte";
  import Login from "./pages/Login.svelte";
  import Write from "./pages/Write.svelte";
  import Singup from "./pages/Singup.svelte";
  import Router from "svelte-spa-router";
  import NotFound from "./pages/NotFound.svelte";
  import "./css/style.css";

  const routes = {
    "/": Main,
    "/login": Login,
    "/signup": Singup,
    "/write": Write,
    "*": NotFound,
  };
</script>

<Router {routes} />
