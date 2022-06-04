<template>
  <header>
      <section>
            <basic-button
                class="open-close"
                :type="'menu'"
                :text="!closeNav ? 'X' : '>'"
                @click.native="closeNav = !closeNav"
            />
            <picture>
                <img src="/img/logo.png" alt="logo" width="80" height="40">
            </picture>
            <basic-button 
                class="exit"
                :type="'button'"
                :text="'Salir'"
            />
            <nav-buyer
                class="nav"
                :class="{'open': !closeNav}"
            />
      </section>
  </header>
</template>

<script>
export default {
    data() {
        return {
            closeNav: true
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
        max-width: 100vw
        z-index: 10

    section
        position: relative
        display: grid
        grid-template-columns: repeat(3, 1fr)
        padding: 1rem 2rem
        max-width: calc( 100vw - 4rem )
        width: calc( 100vw - 4rem )
        height: -webkit-fill-available
        box-shadow: 0px 0px 5px #333
        max-width: 100vw
        z-index: 2

    picture
        grid-column: 2 / 3
        justify-self: center


    .nav
        margin-left: -100%
        transition: margin-left 1s 

    .open
        margin-left: 0

    .exit
        justify-self: flex-end
        align-self: center

    .open-close
        align-self: center
            
</style>