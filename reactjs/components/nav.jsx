import React from "react"
import Test1 from "./Test1"

export default class Nav extends React.Component {
  render() {
    let styles = {
      nav: {
        float: 'left',
        height: '100%',
        width: '25%',
        position: 'fixed',
        zIndex: '+1'
      },
      menu: {
        width: '100%',
        position: 'relative',
      }
    }
    return (
      <nav style={styles.nav}>
        <div style={styles.menu}>
          <p>hi</p>
        </div>

      </nav>
    )
  }
}
