import { createSlice, nanoid, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

const ITEMS_URL = process.env.REACT_APP_API_URL+'/posts';
// const ITEMS_URL = 'http://localhost:8100'+'/posts';


const initialState = {
    posts: [],
    status: 'idle', //'idle' | 'loading' | 'succeeded' | 'failed'
    error: null  
}


// *******************************************************************************
// *******************************************************************************
export const fetchPosts = createAsyncThunk('posts/fetchPosts', async () => {
    try {
        const response = await axios.get(ITEMS_URL)
        return [...response.data];
        // return response.data
    } catch (err) {
        return err.message;
    }
})

export const fetchPostById = createAsyncThunk('posts/fetchPostById', async (initialPost) => {
    const { id } = initialPost;
    try {
        const response = await axios.get(`${ITEMS_URL}/${id}`)
        // return [...response.data];
        return response.data
    } catch (err) {
        return err.message;
    }
})

export const addNewPost = createAsyncThunk('posts/addNewPost', async (initialPost) => {
    try {
        const response = await axios.post(`${ITEMS_URL}/add`, initialPost)
        return response.data
    } catch (err) {
        return err.message;
    }
})

export const updatePost = createAsyncThunk('posts/updatePost', async (initialPost) => {
    const { id } = initialPost;
    try {
        const response = await axios.put(`${ITEMS_URL}/update/${id}`, initialPost)
        return response.data
    } catch (err) {
        //return err.message;
        return initialPost; // only for testing Redux!
    }
})

export const updateSomePosts = createAsyncThunk('posts/updateSomePosts', async (initialPost) => {
    // const { id } = initialPost;
    try {
        const response = await axios.put(`${ITEMS_URL}/update_posts/0`, initialPost)
        return response.data
    } catch (err) {
        //return err.message;
        return initialPost; // only for testing Redux!
    }
})
// 
export const deletePost = createAsyncThunk('posts/deletePost', async (initialPost) => {
    const { id } = initialPost;
    try {
        const response = await axios.delete(`${ITEMS_URL}/${id}`)
        if (response?.status === 200) return initialPost;
        return `${response?.status}: ${response?.statusText}`;
    } catch (err) {
        return err.message;
    }
})
// *******************************************************************************
// *******************************************************************************


const postsSlice = createSlice({
    name:'posts',
    initialState,
    reducers: {
        postAdded: {
            reducer(state, action) {
                state.posts.push(action.payload)
            },
        }
    },
    extraReducers(builder) {
        builder
            .addCase(fetchPosts.pending, (state, action) => {
                state.status = 'loading'
            })
            .addCase(fetchPosts.fulfilled, (state, action) => {
                state.status = 'succeeded'                
                // Add any fetched posts to the array
                
                state.posts = action.payload
            })
            .addCase(fetchPosts.rejected, (state, action) => {
                state.status = 'failed'
                state.error = action.error.message
            })                  
            .addCase(fetchPostById.fulfilled, (state, action) => {                
                state.status = 'succeeded'
                state.posts = action.payload
            })
            .addCase(addNewPost.fulfilled, (state, action) => {
                state.status = 'succeeded'                  
                state.posts.push(action.payload)
            })
            .addCase(updatePost.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Update could not complete')
                    console.log(action.payload)
                    return;
                }
                const { id } = action.payload;
                const updatedIndex = state.posts.findIndex(a => a.id == id);
                state.posts[updatedIndex] = action.payload;
            })
            .addCase(updateSomePosts.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Update could not complete')
                    console.log(action.payload)
                    return;
                }
                // const { id } = action.payload;
                // const updatedIndex = state.posts.findIndex(a => a.id == id);
                // state.posts[updatedIndex] = action.payload;
            })
            .addCase(deletePost.fulfilled, (state, action) => {
                if (!action.payload?.id) {
                    console.log('Delete could not complete')
                    console.log(action.payload)
                    return;
                }
                const { id } = action.payload;
                const accs = state.posts.filter(at => at.id !== id);
                state.posts = accs;
            })
            .addCase(deletePost.rejected, (state, action) => {
                state.status = 'failed'
                state.error = action.error.message
            })
    }
})

export const selectAllPosts = (state) => state.posts.posts;
export const getPostsStatus = (state) => state.posts.status;
export const getPostsError = (state) => state.posts.error;

export const selectPostById = (state, aId) =>  state.posts.posts.find(a => a.id === aId);

 
export const {postAdded} = postsSlice.actions;

export default postsSlice.reducer