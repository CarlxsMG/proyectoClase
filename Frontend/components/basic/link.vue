<template>
  <NuxtLink :to="href">
    {{text}}
  </NuxtLink>
</template>

<script>
export default {
    props: ['href', 'text']
}
</script>

<style lang="sass" scoped>

</style>