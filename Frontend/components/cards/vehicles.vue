<template>
  <section>
      <template v-if="item.branch">
            <picture>
                <img :src="item.image" alt="truck">
            </picture>
            <article>
                <p class="brand">{{item.branch}} {{item.model}}</p>
                <p class="price">{{item.price}}$</p>
            </article>
      </template>
      <template v-else>
          <NuxtLink class="box" to="/seller/vehicle/new">
            <picture class="noImage-pic">
                <img src="/img/trucks/no-image.jpg" alt="truck">
            </picture>
            <article>
                <p class="noImage-text">Añadir vehiculo</p>
            </article>
          </NuxtLink>
      </template>
  </section>
</template>

<script>
export default {
    props: {
        item: {
            type: Object,
            required: false,
            default: () => ({})
        }
    }
}
</script>

<style lang="sass" scoped>
    .box
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

    .noImage
        &-pic img
            width: 100%

        &-text
            align-self: center
            color: #fff
            font-weight: bold

    
            
</style>