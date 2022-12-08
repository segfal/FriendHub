import React,{useState,useEffect} from "react";
import axios from "axios";



const SignUp = (props : any) =>
{
    const [getUsername,setUsername] = useState('');
    const [getPassword,setPassword] = useState('');
    const [getPassword2,setPassword2] = useState('');
    const [getErr,setErr] = useState(false);
    const [getErrMessage,setErrMessage] = useState('');
    const [getLoading,setLoading] = useState(true);
    const [getSuccess,setSuccess] = useState(false);
    const [getSuccessMessage,setSuccessMessage] = useState('');
    const [getRedirect,setRedirect] = useState(false);
    const [getRedirectMessage,setRedirectMessage] = useState('');
    const [getRedirectLink,setRedirectLink] = useState('');

    const submit = async () =>
    {
        setLoading(false);
        if(getPassword != getPassword2)
        {
            setErr(true);
            setErrMessage('Passwords do not match');
        }
        else
        {
            const data = {
                username : getUsername,
                password : getPassword
            }
            const response = await axios.post('http://localhost:3000/api/signup',data);
            const json = await response.data;
            if(json.success)
            {
                setSuccess(true);
                setSuccessMessage(json.message);
                setRedirect(true);
                setRedirectMessage('Redirecting to login page');
                setRedirectLink('/login');
            }
            else
            {
                setErr(true);
                setErrMessage(json.message);
            }
        }
    }

    useEffect(() =>
    {
        if(getRedirect)
        {
            setTimeout(() =>
            {
                window.location.href
            },3000);

        }
    },[getRedirect]);

}





export default SignUp;