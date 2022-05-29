<template>
  <footer>
      <section>
          <picture>
              <img src="/img/logo.png" alt="logo" width="80" height="40">
          </picture>
          <small>Truckers 2021-2022 ~ powered by CarlosMartinez.</small>
      </section>
  </footer>
</template>

<script>
export default {

}
</script>

<style lang="sass" scoped>
    footer
        background: #fff
        box-shadow: 0px -1px 5px #333
        padding: 1rem 2rem

        section
            display: grid
            grid-template-columns: repeat(2, 1fr)

            picture
                grid-column: 1 / 2

            small
                grid-column: 2 / -1
                justify-self: flex-end
                align-self: center
                font-style: italic
                text-align: right
</style>