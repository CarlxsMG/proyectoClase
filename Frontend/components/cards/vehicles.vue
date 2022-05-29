<template>
  <section>
      <picture>
          <img src="/img/trucks/red.jpg" alt="truck">
      </picture>
      <article>
          <p class="brand">Marca Modelo</p>
          <p class="price">50000$</p>
      </article>
  </section>
</template>

<script>
export default {

}
</script>

<style lang="sass" scoped>
    section
        max-width: 200px
        max-height: 200px
        min-width: 200px
        min-height: 200px
        border-radius: 1rem
        box-shadow: 0 0 10px #ccc

        display: grid
        grid-template-columns: 1fr
        grid-template-rows: 1fr
        overflow: hidden
        cursor: pointer

        img
            height: 100%

        article
            align-self: flex-end
            display: grid
            grid-template-columns: repeat(2, auto)
            justify-content: space-between
            background: #33333333
            height: fit-content
            background: #333333cc
            padding: .5rem

    .brand, .price
        align-self: flex-end
        color: #eee
        font-weight: bold

    
            
</style>