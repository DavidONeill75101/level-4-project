import '../styles/globals.css'
import Search from './search';
import React, { useState, useEffect} from 'react';
import {useRouter} from "next/router";

function MyApp({ Component, pageProps }) {
    
  return(
    <div>
      <Search />
      
     
    </div>
  )
}
export default MyApp
