<template>
  <header>
      <section>
            <basic-button
                :type="'menu'"
                :text="'>'"
            />
            <picture>
                <img src="/img/logo.png" alt="logo" width="80" height="40">
            </picture>
            <basic-button 
                class="login"
                :type="'button'"
                :text="'Entrar | Registrarme'"
            />
            <nav-seller />
      </section>
  </header>
</template>

<script>
export default {

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
        max-width: 100vw

    section
        position: relative
        display: grid
        grid-template-columns: repeat(3, 1fr)
        padding: 1rem 2rem
        width: 100vw
        height: 100%
        height: fit-content
        box-shadow: 0px 0px 5px #333
        max-width: 100vw
        z-index: 2

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