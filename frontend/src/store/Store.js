import { configureStore, combineReducers } from "@reduxjs/toolkit";
import authsReducer from "../reducers/AuthSlice";
import individualsReducer from "../reducers/IndividualSlice";
import postsReducer from "../reducers/PostSlice";
import familiesReducer from "../reducers/FamilySlice";

// import storage from 'redux-persist/lib/storage';
import storageSession from "redux-persist/lib/storage/session";
import { persistReducer, persistStore } from "redux-persist";
import thunk from "redux-thunk";

const persistConfig = {
  key: "root",
  storage: storageSession,
  blacklist: [
     "auths", "individuals", "posts", "families"
  ],
};

const rootReducer = combineReducers({
  auths:authsReducer,
  individuals: individualsReducer,
  posts: postsReducer,
  families: familiesReducer,
});

const persistedReducer = persistReducer(persistConfig, rootReducer);

export const Store = configureStore({
  reducer: persistedReducer,
  middleware: [thunk],
});

// export const store = configureStore({
//   reducer: persistedReducer,
//   devTools: process.env.NODE_ENV !== 'production',
//   middleware: [thunk]
// })

export const persistor = persistStore(Store);
