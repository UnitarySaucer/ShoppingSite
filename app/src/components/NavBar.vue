<template>
  <header>
    <h1 class="title">Shopping Site</h1>
    <nav>
      <ul class="nav_links">
        <!-- <li class="nav-text site-name"><a href="#">Shopping Site</a></li> -->
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Log In/Register</a></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap');

li, a {
  font-family: 'Josefin Sans', sans-serif;
  font-weight: 400;
  font-size: 2.25rem;
  color: black;
  text-decoration: none;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.875rem 10%;
  background: #C4C4C4;
  height: 5rem;
}

.title{
  cursor: pointer;
  font-family: 'Josefin Sans', sans-serif;
  font-weight: 400;
  font-size: 2.25rem;
}

.nav_links {
  list-style: none;
}

.nav_links li {
  display: inline-block;
  padding: 0 1.25rem;
}
.nav_links li a, h1{
  transition: all 0.3s ease 0s;
}

.nav_links li a:hover, h1:hover {
  color: rgb(3, 179, 223);
}

</style>