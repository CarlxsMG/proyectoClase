<template>
  <form class="form" id="form-vehicle" @submit.prevent="editOrCreate">
    <section class="form-sect">
        <label class="form-sect-label" style="font-weight: bold;" for="picture">Imagen: <br>
        <input class="form-sect-input" type="text" name="picture" id="picture" :value="result.picture || ''">
        <img class="form-sect-pic" :src="result.picture || '/img/trucks/no-image.jpg'" id="pic" />
        </label>
    </section>
      
      <section class="form-section">
            <label class="form-section-brand" for="brand">
                Marca: <br>
                <input type="text" name="brand" id="brand" :value="result.brand || ''">
            </label>
            <label class="form-section-model" for="model">
                Modelo: <br>
                <input type="text" name="model" id="model" :value="result.model || ''">
            </label>
            <label class="form-section-price" for="price">
                Precio: <br>
                <input type="number" name="price" id="price" :value="result.price || ''">
            </label>
            <label class="form-section-plate" for="plate">
                Matricula: <br>
                <input type="text" name="plate" id="plate" :value="result.plate || ''">
            </label>
            <label class="form-section-description" for="description">
                Descripción: <br>
                <textarea name="description" id="description" :value="result.description || ''"></textarea>
            </label>
            <input type="text" style="display:none;" name="owner" :value="user">
            <input type="text" style="display:none;" name="status" :value="result.status || 'A'">
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
    async beforeMount() {
        if(this.$route.params.id != 'new') {
            const req = await this.$axios.get(`vehicle/${this.$route.params.id}`)
            this.result = req.data

        }
    },
    data() {
        let user = this.$store.state.auth.user.user_id
        
        return {
            result: {},
            user: user
        }
    },
    methods: {
        async editOrCreate() {
            if(this.$route.params.id != 'new') {
                const form = document.querySelector('#form-vehicle')
                const formData = new FormData(form)
    
                const res = await this.$axios.put(`vehicle/${this.$route.params.id}/`, formData)
                
                if(res.status == 200) {
                    this.$router.push('/seller/vehicle')
                }
            }
            else {
                const form = document.querySelector('#form-vehicle')
                const formData = new FormData(form)
    
                const res = await this.$axios.post(`vehicle/`, formData)
                
                if(res.status == 201) {
                    this.$router.push('/seller/vehicle')
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

        &-sect
            display: grid

            &-label
                font-weight: bold

            &-input
                padding: .5rem
                border: 1px solid #ccc
                border-radius: 4px
                margin-bottom: .5rem
                width: 90%

            &-pic
                min-width: 250px
                min-height: 250px
                max-width: 250px
                max-height: 250px
                border-radius: 50%
                border: 4px solid #000                

        &-section
            display: grid
            gap: 1rem
            padding: 2rem 1rem

            &-brand, &-model, &-price, &-plate, &-description
                font-weight: bold

                input
                    padding: .5rem
                    border: 1px solid #ccc
                    border-radius: 4px
                    width: 90%
                
                textarea
                    padding: .5rem
                    border: 1px solid #ccc
                    border-radius: 4px
                    width: 90%
                    height: 10rem
        &-submit
            margin: 1rem
</style>