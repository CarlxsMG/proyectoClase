<template>
  <nav>
      <p>Panel vendedores.</p>
      <ul>
        <li>
            <NuxtLink to="/seller">
              Mi Panel
            </NuxtLink>
        </li>
        <li>
            <NuxtLink to="/seller/vehicle">
              Vehiculos
            </NuxtLink>
        </li>
        <li>
            <NuxtLink to="/seller/trade">
              Peticiones
            </NuxtLink>
        </li>
        <li>
            <NuxtLink to="/seller/contract">
              Contratos
            </NuxtLink>
        </li>
        <li>
            <NuxtLink to="/seller/payment">
              Pagos
            </NuxtLink>
        </li>
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
        top: 74px
        box-shadow: inset 2px 0px 4px #333
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
                padding-top: 1.5rem
</style>