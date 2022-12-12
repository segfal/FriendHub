import React,{useEffect,useState} from 'react';
import axios from 'axios';
import styles from '../styles/Home.module.css'
import Router from 'next/router';
import {useRouter} from 'next/router';

const ChatBox = () =>
{
  
}







const App = () => 
{
  const [data,setData] = useState('null');


  useEffect(
    () =>
    {
      axios.get('http://127.0.0.1:5000/insert/hello/world').then(
        (res) =>
        {
          setData(res.data)
          console.log(res.data)
        }

      )
    }
  )
  return(
    <div>
    <div className={styles.container}>
      <div className={styles.box2}>
              <h1>
        😎FriendHub😎
        </h1>
        </div>
        </div>
        <div className={styles.container}>
          <div className={styles.box}>
            <h1>
              {data}
            </h1>

            <h2>
              Welcome
            </h2>
            <input  type="text" placeholder="Username"/>
        
            <br/>
            <button>
              Login
            </button>
            <br/>
          

          </div>



        </div>
  
    </div>
  );

}




export default App;