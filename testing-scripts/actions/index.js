import axios from 'axios';

//now we have different user types that we will fetch,
//
import { FETCH_USER, LOGOUT, FETCH_SURVEYS } from './types';



export const fetchSurveys = () => async dispatch => {
  const res = await axios.get('/api/surveys');

  dispatch( { type: FETCH_SURVEYS, payload: res.data})
}

// so function() return function () {}
// is the same as
// () => (dispatch) => {}
export const fetchUser = function(){

  return  async dispatch => {

    const res = await axios.get('/api/current-user');
    dispatch({ type: FETCH_USER, payload: res.data });
  };

}

export const logout = function(){

  return  async dispatch => {

    const res = await axios.get('/api/logout');
    dispatch({ type: LOGOUT, payload: res.data });
    // window.location.href="/";
  };

}

export const handleToken = (token) => async dispatch => {

  const res = await axios.post('/api/stripe',token);
  dispatch({ type: FETCH_USER, payload: res.data });

}


export const submitSurvey = (formValues, history)  => async dispatch => {
  const res = await axios.post("/api/surveys",formValues);
  // dispatch({ type: SURVEY_SENT, payload: res.data})
  history.push('/surveys'); // redirect user ack to dashboard
  dispatch({ type: FETCH_USER, payload: res.data });
  return { type: 'submit_survey' }
}
