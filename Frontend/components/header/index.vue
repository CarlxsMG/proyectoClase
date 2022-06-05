<template>
  <header>
      <section>
          <picture>
              <img src="/img/logo.png" alt="logo" width="80" height="40">
          </picture>
          <basic-button
            @click.native="openPopup"
            class="login"
            :type="'button'"
            :text="'Entrar'"
          />
      </section>
  </header>
</template>

<script>
export default {
    methods: {
        openPopup() {
            this.$store.commit('popup/open', !this.$store.state.popup.open)
        }
    }
}
</script>

<style lang="sass" scoped>
    header
        position: fixed
        top: 0
        left: 0
        background: #fff
        max-height: 74px
        height: 74px
        min-height: 74px
        z-index: 10


    section
        display: grid
        grid-template-columns: repeat(3, 1fr)
        padding: 1rem 2rem
        max-width: calc( 100vw - 4rem )
        width: calc( 100vw - 4rem )
        height: -webkit-fill-available
        box-shadow: 0px 0px 5px #333

    picture
        grid-column: 2 / 3
        justify-self: center

        @media screen and (max-width: 768px) 
            grid-column: 1 / 2


    .login
        grid-column: 3 / -1
        justify-self: flex-end
        align-self: center

            
</style>