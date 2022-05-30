<template>
  <nav>
      <p>Panel vendedores.</p>
      <ul>
          <li>Mi Panel</li>
          <li>Vehiculos</li>
          <li>Peticiones</li>
          <li>Contratos</li>
          <li>Pagos</li>
      </ul>
  </nav>
</template>

<script>
export default {

}
</script>

<style lang="sass" scoped>
    nav
        width: fit-content
        max-width: 300px
        display: grid
        grid-template-rows: auto 1fr
        border-right: 1px solid #ccc
        position: fixed
        top: 77px
        left: 0
        background: #fff
        z-index: 1
        height: calc(100vh - 74px)
        padding: 1rem

        p
            font-size: 2rem

        ul
            list-style: none

            li
                padding: .5rem 1rem
                border-bottom: 1px solid #ccc
</style>