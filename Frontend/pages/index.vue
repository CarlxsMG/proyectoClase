<template>
  <article class="main">
      <section class="main-about">
          <hgroup class="main-about-title">
              <h1>Truckers.</h1>
          </hgroup>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque impedit sapiente sit repudiandae voluptatem hic rem consectetur nulla? Nemo doloribus cum, reiciendis inventore molestiae ab quia laudantium voluptatem velit! Ducimus?</p>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime vel ad molestiae nemo sit inventore repellat dicta id aut at quos facilis debitis, magnam a obcaecati architecto, corrupti, assumenda libero.</p>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime vel ad molestiae nemo sit inventore repellat dicta id aut at quos facilis debitis, magnam a obcaecati architecto, corrupti, assumenda libero. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestiae harum, sunt quam inventore iusto provident hic. Illum nulla quaerat modi natus repellendus inventore fugit molestiae, harum reprehenderit omnis, excepturi sapiente.</p>
            <basic-button 
                class="main-about-button"
                :type="'button'"
                :text="'Contactar'"
            />
      </section>
  </article>
</template>

<script>
export default {
    layout: 'base'
}
</script>

<style lang="sass" scoped>
    .main
        margin-top: 74px
        background: url('static/img/main.jpg')no-repeat
        min-height: calc(100vh - 74px)

        display: grid
        grid-template-columns: 1fr

        @media screen and (min-width: 1024px)
            grid-template-columns: repeat(2, 1fr)


        &-vehicles
            display: flex
            gap: 2rem
            justify-content: center
            padding: 4rem
            flex-wrap: wrap


            &-item
                justify-self: center
        
        &-more
            font-weight: bold
            color: #fff
            text-decoration: underline
            width: fit-content
            height: fit-content
            background: #333333ee
            justify-self: center
            align-self: center
            padding: 1rem
            margin: 1rem
            border-radius: 10px
            box-shadow: 0 0 10px #ccc

        &-about
            padding: 5rem
            background: #00000099
            display: grid
            grid-template-rows: auto
            max-height: 900px
            color: #fff

            &-title
                h1
                    text-align: center
                    font-size: 3rem
                    font-weight: bold
                    text-decoration: underline 

                    @media screen and (min-width: 1024px)
                        padding-bottom: 2rem

            &-button
                align-self: flex-end
                justify-self: center
                background: #fff
</style>