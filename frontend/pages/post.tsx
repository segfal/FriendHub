import React from "react";
import styles from '../styles/Home.module.css'
import Router from "next/router";



const table = () =>
{

    const recfun = (name : String , about : String) =>
    {
        return {
            0 : 'Hello',
            1 : 'There'
        }
    }
    const posts = [

    ]
}



const Post = () => 
{

    return (
        <div>
            <title>
                Friendster
            </title>
            <div>
                <div className={styles.container}>
                    
                        
                  <div className={styles.box}>
                    <h1>
                        Hello Admin
                    </h1>

                    <h1>
                        😎😎😎😎😎😎😎😎
                    </h1>
                    </div>
                    <br/>
                    <div className={styles.box}>
                    <h1>
                        Hello Admin
                    </h1>

                 

                    <h1>
                        😎😎😎😎😎😎😎😎
                    </h1>
                    </div>
                </div>

            </div>
        </div>
    );
}


export default Post;