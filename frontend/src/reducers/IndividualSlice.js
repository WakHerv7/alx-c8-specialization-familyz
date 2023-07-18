import { createSlice, nanoid, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

const ITEMS_URL = process.env.REACT_APP_API_URL+'/individuals';
// const ITEMS_URL = 'http://localhost:8100'+'/individuals';


const initialState = {
    individuals: [],
    status: 'idle', //'idle' | 'loading' | 'succeeded' | 'failed'
    error: null  
}


// *******************************************************************************
// *******************************************************************************
export const fetchIndividuals = createAsyncThunk('individuals/fetchIndividuals', async () => {
    try {
        const response = await axios.get(ITEMS_URL+'/list')
        // return [...response.data.family];
        return response.data
    } catch (err) {
        return err.message;
    }
})

export const fetchIndividualById = createAsyncThunk('individuals/fetchIndividualById', async (initialIndividual) => {
    const { id } = initialIndividual;
    try {
        const response = await axios.get(`${ITEMS_URL}/${id}`)
        // return [...response.data];
        return response.data
    } catch (err) {
        return err.message;
    }
})

export const addNewIndividual = createAsyncThunk('individuals/addNewIndividual', async (initialIndividual) => {
    try {
        const response = await axios.post(`${ITEMS_URL}/add`, initialIndividual)
        return response.data
    } catch (err) {
        return err.message;
    }
})

export const updateIndividual = createAsyncThunk('individuals/updateIndividual', async (initialIndividual) => {
    const { id } = initialIndividual;
    try {
        const response = await axios.put(`${ITEMS_URL}/update/${id}`, initialIndividual)
        return response.data
    } catch (err) {
        //return err.message;
        return initialIndividual; // only for testing Redux!
    }
})

export const updateSomeIndividuals = createAsyncThunk('individuals/updateSomeIndividuals', async (initialIndividual) => {
    // const { id } = initialIndividual;
    try {
        const response = await axios.put(`${ITEMS_URL}/update_individuals/0`, initialIndividual)
        return response.data
    } catch (err) {
        //return err.message;
        return initialIndividual; // only for testing Redux!
    }
})
// 
export const deleteIndividual = createAsyncThunk('individuals/deleteIndividual', async (initialIndividual) => {
    const { id } = initialIndividual;
    try {
        const response = await axios.delete(`${ITEMS_URL}/${id}`)
        if (response?.status === 200) return initialIndividual;
        return `${response?.status}: ${response?.statusText}`;
    } catch (err) {
        return err.message;
    }
})
// *******************************************************************************
// *******************************************************************************


const individualsSlice = createSlice({
    name:'individuals',
    initialState,
    reducers: {
        individualAdded: {
            reducer(state, action) {
                state.individuals.push(action.payload)
            },
        }
    },
    extraReducers(builder) {
        builder
            .addCase(fetchIndividuals.pending, (state, action) => {
                state.status = 'loading'
            })
            .addCase(fetchIndividuals.fulfilled, (state, action) => {
                state.status = 'succeeded'                
                // Add any fetched individuals to the array
                
                state.individuals = action.payload
            })
            .addCase(fetchIndividuals.rejected, (state, action) => {
                state.status = 'failed'
                state.error = action.error.message
            })                  
            .addCase(fetchIndividualById.fulfilled, (state, action) => {                
                state.status = 'succeeded'
                state.individuals = action.payload
            })
            .addCase(addNewIndividual.fulfilled, (state, action) => {
                state.status = 'succeeded'                  
                state.individuals.push(action.payload)
            })
            .addCase(updateIndividual.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Update could not complete')
                    console.log(action.payload)
                    return;
                }
                const { id } = action.payload;
                const updatedIndex = state.individuals.findIndex(a => a.id == id);
                state.individuals[updatedIndex] = action.payload;
            })
            .addCase(updateSomeIndividuals.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Update could not complete')
                    console.log(action.payload)
                    return;
                }
                // const { id } = action.payload;
                // const updatedIndex = state.individuals.findIndex(a => a.id == id);
                // state.individuals[updatedIndex] = action.payload;
            })
            .addCase(deleteIndividual.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Delete could not complete')
                    console.log(action.payload)
                    return;
                }
                const { id } = action.payload;
                const accs = state.individuals.filter(at => at.id !== id);
                state.individuals = accs;
            })
            .addCase(deleteIndividual.rejected, (state, action) => {
                state.status = 'failed'
                state.error = action.error.message
            })
    }
})

export const selectAllIndividuals = (state) => state.individuals.individuals;
export const getIndividualsStatus = (state) => state.individuals.status;
export const getIndividualsError = (state) => state.individuals.error;

export const selectIndividualById = (state, aId) =>  state.individuals.individuals.find(a => a.id === aId);

 
export const {individualAdded} = individualsSlice.actions;

export default individualsSlice.reducer