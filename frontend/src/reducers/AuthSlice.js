import { createSlice, nanoid, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

const ITEMS_URL = process.env.REACT_APP_API_URL+'/auths';
const ITEMS_URL2 = process.env.REACT_APP_API_URL+'/individuals';

const initialState = {
    auths: [],
    status: 'idle', //'idle' | 'loading' | 'succeeded' | 'failed'
    error: null  
}


// *******************************************************************************
// *******************************************************************************
export const fetchAuths = createAsyncThunk('auths/fetchAuths', async () => {
    try {
        const response = await axios.get(ITEMS_URL)
        return [...response.data];
    } catch (err) {
        return err.message;
    }
})

export const fetchAuthById = createAsyncThunk('auths/fetchAuthById', async (initialAuth) => {
    const { id } = initialAuth;
    try {
        const response = await axios.get(`${ITEMS_URL2}/${id}`)
        // return [...response.data];
        return response.data
    } catch (err) {
        return err.message;
    }
})

export const addNewAuth = createAsyncThunk('auths/addNewAuth', async (initialAuth) => {
    try {
        const response = await axios.post(ITEMS_URL, initialAuth)
        return response.data
    } catch (err) {
        return err.message;
    }
})

export const updateAuth = createAsyncThunk('auths/updateAuth', async (initialAuth) => {
    const { id } = initialAuth;
    try {
        const response = await axios.put(`${ITEMS_URL}/${id}`, initialAuth)
        return response.data
    } catch (err) {
        //return err.message;
        return initialAuth; // only for testing Redux!
    }
})

export const updateSomeAuths = createAsyncThunk('auths/updateSomeAuths', async (initialAuth) => {
    // const { id } = initialAuth;
    try {
        const response = await axios.put(`${ITEMS_URL}/update_auths/0`, initialAuth)
        return response.data
    } catch (err) {
        //return err.message;
        return initialAuth; // only for testing Redux!
    }
})
// 
export const deleteAuth = createAsyncThunk('auths/deleteAuth', async (initialAuth) => {
    const { id } = initialAuth;
    try {
        const response = await axios.delete(`${ITEMS_URL}/${id}`)
        if (response?.status === 200) return initialAuth;
        return `${response?.status}: ${response?.statusText}`;
    } catch (err) {
        return err.message;
    }
})
// *******************************************************************************
// *******************************************************************************


const authsSlice = createSlice({
    name:'auths',
    initialState,
    reducers: {
        authAdded: {
            reducer(state, action) {
                state.auths.push(action.payload)
            },
        }
    },
    extraReducers(builder) {
        builder
            .addCase(fetchAuths.pending, (state, action) => {
                state.status = 'loading'
            })
            .addCase(fetchAuths.fulfilled, (state, action) => {
                state.status = 'succeeded'                
                // Add any fetched auths to the array
                
                state.auths = action.payload
            })
            .addCase(fetchAuths.rejected, (state, action) => {
                state.status = 'failed'
                state.error = action.error.message
            })                  
            .addCase(fetchAuthById.fulfilled, (state, action) => {                
                state.status = 'succeeded'
                state.auths = action.payload
            })
            .addCase(addNewAuth.fulfilled, (state, action) => {
                state.status = 'succeeded'                  
                state.auths.push(action.payload)
            })
            .addCase(updateAuth.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Update could not complete')
                    console.log(action.payload)
                    return;
                }
                const { id } = action.payload;
                const updatedIndex = state.auths.findIndex(a => a.id == id);
                state.auths[updatedIndex] = action.payload;
            })
            .addCase(updateSomeAuths.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Update could not complete')
                    console.log(action.payload)
                    return;
                }
                // const { id } = action.payload;
                // const updatedIndex = state.auths.findIndex(a => a.id == id);
                // state.auths[updatedIndex] = action.payload;
            })
            .addCase(deleteAuth.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Delete could not complete')
                    console.log(action.payload)
                    return;
                }
                const { id } = action.payload;
                const accs = state.auths.filter(at => at.id !== id);
                state.auths = accs;
            })
            .addCase(deleteAuth.rejected, (state, action) => {
                state.status = 'failed'
                state.error = action.error.message
            })
    }
})

export const selectAllAuths = (state) => state.auths.auths;
export const getAuthsStatus = (state) => state.auths.status;
export const getAuthsError = (state) => state.auths.error;

export const selectAuthById = (state, aId) =>  state.auths.auths.find(a => a.id === aId);

 
export const {authAdded} = authsSlice.actions;

export default authsSlice.reducer