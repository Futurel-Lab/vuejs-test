<template>
  <div class="home-page">
    <h1>Welcome to the Home Page</h1>
    <a href="/games">Games Library</a>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {
      message: "Hello, Vue 3!",
    };
  },
};
</script>

<style scoped>
.home-page {
  text-align: center;
  margin-top: 50px;
}
</style>
