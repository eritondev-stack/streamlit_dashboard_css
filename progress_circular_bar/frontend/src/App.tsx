import React, { useEffect } from 'react';
import { withStreamlitConnection, Streamlit, ComponentProps } from "streamlit-component-lib"
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

const Component = ({ args }: ComponentProps) => {

  const { value, width, textColor,pathColor,trailColor, strokeWidth  } = args

  useEffect(() => Streamlit.setFrameHeight())

  //Streamlit.setComponentValue({})

  return (
    <div className='flex justify-center'>
      <div style={{ width: `${width}px`}}>
        <CircularProgressbar
          strokeWidth={strokeWidth}
          value={value}
          text={`${Number(value).toFixed(0)}%`}
          styles={buildStyles({
            textColor: textColor,
            pathColor: pathColor,
            trailColor: trailColor
          })}
        />
      </div>
    </div>
  )
}

export default withStreamlitConnection(Component)