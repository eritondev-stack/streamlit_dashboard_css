import React, { useEffect } from 'react';
import { withStreamlitConnection, Streamlit, ComponentProps } from "streamlit-component-lib"
import parse from 'html-react-parser';
import './index.css'
const Component = ({ args }: ComponentProps) => {

  const { html } = args

  useEffect(() => Streamlit.setFrameHeight())

  //Streamlit.setComponentValue({})

  return (
    <>
    {parse(html)}
    </>
    
  )
}

export default withStreamlitConnection(Component)