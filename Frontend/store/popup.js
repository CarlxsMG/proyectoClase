export const state = () => ({
    open: false
})

export const mutations = {
    open(state, value){
        state.open = value
    }
}

export const strict = false
