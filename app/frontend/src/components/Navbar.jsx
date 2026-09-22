import { Link, NavLink } from "react-router-dom";

function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar-inner">

        <Link
          to="/"
          className="brand"
        >
          <span className="brand-icon">🌿</span>

          <span>
            Plant<span>AI</span>
          </span>
        </Link>

        <nav className="nav-links">

          <NavLink
            to="/"
            className={({ isActive }) =>
              isActive ? "nav-link active" : "nav-link"
            }
          >
            Home
          </NavLink>

          <NavLink
            to="/analyze"
            className={({ isActive }) =>
              isActive ? "nav-link active" : "nav-link"
            }
          >
            Analyze
          </NavLink>

          <Link
            to="/analyze"
            className="nav-cta"
          >
            Analyze Plant
          </Link>

        </nav>

      </div>
    </header>
  );
}

export default Navbar;