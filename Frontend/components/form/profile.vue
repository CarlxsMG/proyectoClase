<template>
  <form class="form" id="form-profile" @submit.prevent="editOrCreate">      
      <section class="form-section">
            <label class="form-section-name" for="first_name">
                Nombre: <br>
                <input type="text" name="first_name" id="first_name" :value="result.first_name || ''">
            </label>
            <label class="form-section-name" for="last_name">
                Apellido: <br>
                <input type="text" name="last_name" id="last_name" :value="result.last_name || ''">
            </label>
            <label class="form-section-phone" for="phone">
                Teléfono: <br>
                <input type="text" name="phone" id="phone" :value="result.phone || ''">
            </label>
            <label class="form-section-email" for="email">
                Email: <br>
                <input type="email" name="email" id="email" :value="result.email || ''">
            </label>
            <label class="form-section-location">
                Calle: <br>
                <input type="text" name="location" id="location" :value="result.location || ''">
            </label>
            <label class="form-section-pc">
                Código postal: <br>
                <input type="number" name="postal_code" id="postal_code" :value="result.postal_code || ''">
            </label>
            <label class="form-section-doc" for="doc_identifier">
                DNI: <br>
                <input type="text" name="doc_identifier" id="doc_identifier" :value="result.doc_identifier || ''">
            </label>
            <label class="form-section-bank" for="bank">
                Bank: <br>
                <input type="text" name="bank" id="bank" :value="result.bank || ''">
            </label>
            <input type="text" name="username" id="username" style="display: none;" :value="result.username">
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
    props: {
        type_profile: {
            type: String,
            required: true
        }
    },
    async beforeMount() {
        let req
        if(this.type_profile == 'seller') {
            req = await this.$axios.get(`users/seller/${this.$store.state.auth.user.user_id}`)
        }
        else {
            req = await this.$axios.get(`users/buyer/${this.$store.state.auth.user.user_id}`)
        }
        
        this.result = req.data
    },
    data() {
        return {
            result: {}
        }
    },
    methods: {
        async editOrCreate() {
            const form = document.querySelector('#form-profile')
            const formData = new FormData(form)

            let req
            if(this.type_profile == 'seller') {
                req = await this.$axios.put(`users/seller/${this.$store.state.auth.user.user_id}/`, formData)
            }
            else {
                req = await this.$axios.put(`users/buyer/${this.$store.state.auth.user.user_id}/`, formData)
            }
            
            if(req.status == 200) {
                if(this.type_profile == 'seller') {
                    this.$router.push('/seller')
                }
                else {
                    this.$router.push('/buyer')
                }
            }
        }
    }
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