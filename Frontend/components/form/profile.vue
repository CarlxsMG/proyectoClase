<template>
  <form class="form">      
      <section class="form-section">
            <label class="form-section-name" for="name">
                Nombre: <br>
                <input type="text" name="name" id="name">
            </label>
            <label class="form-section-phone" for="phone">
                Teléfono: <br>
                <input type="text" name="phone" id="phone">
            </label>
            <label class="form-section-email" for="email">
                Email: <br>
                <input type="email" name="email" id="email">
            </label>
            <label class="form-section-location">
                Calle: <br>
                <input type="text" name="location" id="location">
            </label>
            <label class="form-section-pc">
                Código postal: <br>
                <input type="number" name="postal_code" id="postal_code">
            </label>
            <label class="form-section-doc" for="doc_identifier">
                DNI: <br>
                <input type="text" name="doc_identifier" id="doc_identifier">
            </label>
            <label class="form-section-bank" for="bank">
                Bank: <br>
                <input type="text" name="bank" id="bank">
            </label>
      </section>
      <basic-button 
        class="form-submit"
        :text="'Guardar'"
        :type="'submit'"
      />
  </form>
</template>

<script>
export default {

}
</script>

<style lang="sass" scoped>
    .form
        margin: 4rem auto
        border: 1px solid #ccc
        box-shadow: 0px 0px 5px #333
        padding: 2rem
        max-width: 300px
        display: grid

        &-section
            display: grid
            gap: 1rem
            padding: 2rem 1rem

            &-name, &-phone, &-price, &-email, &-location, &-pc, &-doc, &-bank
                font-weight: bold

                input
                    padding: .5rem
                    border: 1px solid #ccc
                    border-radius: 4px

        &-submit
            margin: auto
</style>