<template>
  <section>
      <form>
        <label for="username">
          Username: <br>
          <input type="text" placeholder="username" name="username" id="username">
        </label>
        <label for="password">
          Password: <br>
          <input type="password" placeholder="password" name="password" id="password">
        </label>
        <basic-button
          :type="'submit'"
          :text="'Entrar'"
        />
      </form>
  </section>
</template>

<script>
export default {

}
</script>

<style lang="sass" scoped>

  section
    position: fixed
    top: 0
    left: 0
    right: 0
    bottom: 0
    background: #00000099
    backdrop-filter: blur(2px)

    form
      margin: auto
      

</style>