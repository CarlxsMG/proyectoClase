<template>
  <section>
      <section class="blur" @click="closePopup"></section>
      <form id="form-login" @submit.prevent="login">
        <p>Iniciar sesion</p>
        <label for="username">
          Username: <br>
          <input type="text" placeholder="username" form="form-login" name="username" id="username" required>
        </label>
        <label for="password">
          Password: <br>
          <input type="password" placeholder="password" form="form-login" name="password" id="password" required>
        </label>
        <label for="type">
          Tipo de usuario: <br>
          <select name="type" id="type">
            <option value="S">Vendedor</option>
            <option value="B">Comprador</option>
          </select>
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
  methods: {
    async login() {
      try {
        const form = document.querySelector('#form-login')
        const formData = new FormData(form)

        const type = document.querySelector('#type').value

        let user = await this.$axios.post(`login/${type}/`,
          formData
        )
        
        if(user.status == 200) {
          let user_data = user.data
          user_data['user_type'] = type
          
          this.$store.commit('auth/user', user_data)
          
          if(type == 'S') {
            this.$router.push('/seller')
          } 
          else {
            this.$router.push('/buyer')
          }

          // this.$store.commit('popup/open', false)
          
        }
      }
      catch(e) {
        console.log(e)
        // this.$router.push('/')
      }
      
    },
    closePopup() {
      this.$store.commit('popup/open', false)
    }
  }
}
</script>

<style lang="sass" scoped>

  section
    position: fixed
    top: 0
    left: 0
    right: 0
    bottom: 0
    background: #00000044
    backdrop-filter: blur(2px)
    display: grid

    form
      margin: auto
      background: #fff
      min-width: 300px
      height: 450px
      display: grid
      gap: 1rem

      p
        font-size: 1.5rem
        font-weight: bold
        text-align: center

      label
        font-weight: bold
        margin: 0 auto
        display: grid
        width: 80%

        input, select
          padding: .5rem
          border: 1px solid #ccc

        select
          width: 100%

      button
        margin: 0 auto

    .blur
      position: fixed
      top: 0
      left: 0
      right: 0
      bottom: 0
      z-index: -1
      background: #33333355
      backdrop-filter: blur(3px)
      

</style>