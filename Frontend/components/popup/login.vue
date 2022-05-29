<template>
  <section>
      <form>
          <input type="text" placeholder="username" name="username" id="username">
          <input type="password" placeholder="password" name="password" id="password">
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

<style>

</style>