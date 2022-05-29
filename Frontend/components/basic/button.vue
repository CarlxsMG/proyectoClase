<template>
  <button :type="type">
      {{text}}
  </button>
</template>

<script>
export default {
    props: ['type', 'text']
}
</script>

<style lang="sass" scoped>
    button
        padding: .5rem
        font-weight: bold
        color: #333
        border: 1px solid #333
        border-radius: 10px
        box-shadow: 1px 1px 5px #ccc
        height: fit-content
        width: fit-content

        @media screen and (max-width: 768px) 
            font-size: .6rem

        &:hover
            transition: background-color .5s
            background-color: #eee


</style>