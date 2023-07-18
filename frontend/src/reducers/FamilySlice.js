import { createSlice, nanoid, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

const ITEMS_URL = process.env.REACT_APP_API_URL+'/families';
// const ITEMS_URL = 'http://localhost:8100'+'/families';


const initialState = {
    families: [],
    status: 'idle', //'idle' | 'loading' | 'succeeded' | 'failed'
    error: null  
}


// *******************************************************************************
// *******************************************************************************
export const fetchFamilies = createAsyncThunk('families/fetchFamilies', async () => {
    try {
        const response = await axios.get(ITEMS_URL)
        // return [...response.data.family];
        return response.data
    } catch (err) {
        return err.message;
    }
})

export const fetchFamilyById = createAsyncThunk('families/fetchFamilyById', async (initialFamily) => {
    const { id } = initialFamily;
    try {
        const response = await axios.get(`${ITEMS_URL}/${id}`)
        // return [...response.data];
        return response.data
    } catch (err) {
        return err.message;
    }
})

export const addNewFamily = createAsyncThunk('families/addNewFamily', async (initialFamily) => {
    try {
        const response = await axios.post(`${ITEMS_URL}/add`, initialFamily)
        return response.data
    } catch (err) {
        return err.message;
    }
})

export const updateFamily = createAsyncThunk('families/updateFamily', async (initialFamily) => {
    const { id } = initialFamily;
    try {
        const response = await axios.put(`${ITEMS_URL}/update/${id}`, initialFamily)
        return response.data
    } catch (err) {
        //return err.message;
        return initialFamily; // only for testing Redux!
    }
})

export const updateSomeFamilies = createAsyncThunk('families/updateSomeFamilies', async (initialFamily) => {
    // const { id } = initialFamily;
    try {
        const response = await axios.put(`${ITEMS_URL}/update_families/0`, initialFamily)
        return response.data
    } catch (err) {
        //return err.message;
        return initialFamily; // only for testing Redux!
    }
})
// 
export const deleteFamily = createAsyncThunk('families/deleteFamily', async (initialFamily) => {
    const { id } = initialFamily;
    try {
        const response = await axios.delete(`${ITEMS_URL}/${id}`)
        if (response?.status === 200) return initialFamily;
        return `${response?.status}: ${response?.statusText}`;
    } catch (err) {
        return err.message;
    }
})
// *******************************************************************************
// *******************************************************************************


const familiesSlice = createSlice({
    name:'families',
    initialState,
    reducers: {
        familyAdded: {
            reducer(state, action) {
                state.families.push(action.payload)
            },
        }
    },
    extraReducers(builder) {
        builder
            .addCase(fetchFamilies.pending, (state, action) => {
                state.status = 'loading'
            })
            .addCase(fetchFamilies.fulfilled, (state, action) => {
                state.status = 'succeeded'                
                // Add any fetched families to the array
                
                state.families = action.payload
            })
            .addCase(fetchFamilies.rejected, (state, action) => {
                state.status = 'failed'
                state.error = action.error.message
            })                  
            .addCase(fetchFamilyById.fulfilled, (state, action) => {                
                state.status = 'succeeded'
                state.families = action.payload
            })
            .addCase(addNewFamily.fulfilled, (state, action) => {
                state.status = 'succeeded'                  
                state.families.push(action.payload)
            })
            .addCase(updateFamily.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Update could not complete')
                    console.log(action.payload)
                    return;
                }
                const { id } = action.payload;
                const updatedIndex = state.families.findIndex(a => a.id == id);
                state.families[updatedIndex] = action.payload;
            })
            .addCase(updateSomeFamilies.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Update could not complete')
                    console.log(action.payload)
                    return;
                }
                // const { id } = action.payload;
                // const updatedIndex = state.families.findIndex(a => a.id == id);
                // state.families[updatedIndex] = action.payload;
            })
            .addCase(deleteFamily.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Delete could not complete')
                    console.log(action.payload)
                    return;
                }
                const { id } = action.payload;
                const accs = state.families.filter(at => at.id !== id);
                state.families = accs;
            })
            .addCase(deleteFamily.rejected, (state, action) => {
                state.status = 'failed'
                state.error = action.error.message
            })
    }
})

export const selectAllFamilies = (state) => state.families.families;
export const getFamiliesStatus = (state) => state.families.status;
export const getFamiliesError = (state) => state.families.error;

export const selectFamilyById = (state, aId) =>  state.families.families.find(a => a.id === aId);

 
export const {familyAdded} = familiesSlice.actions;

export default familiesSlice.reducer