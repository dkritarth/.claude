import React, { useEffect } from 'react';
import { useSiteRoute } from './useSiteRoute';
import { PAGE_HEADINGS } from './seoMeta';
import { HomePage } from './pages/HomePage';
import { AboutPage } from './pages/AboutPage';
import { ResearchPage } from './pages/ResearchPage';
import { ProjectsPage } from './pages/ProjectsPage';
import { EducationPage } from './pages/EducationPage';
import { NewsPage } from './pages/NewsPage';
import { applyPageSeo } from './seoMeta';

const App: React.FC = () => {
  const page = useSiteRoute();

  useEffect(() => {
    applyPageSeo(page);
    window.scrollTo(0, 0);
  }, [page]);

  const content = (() => {
    switch (page) {
    case 'about':
      return <AboutPage />;
    case 'research':
      return <ResearchPage />;
    case 'projects':
      return <ProjectsPage />;
    case 'education':
      return <EducationPage />;
    case 'news':
      return <NewsPage />;
    default:
      return <HomePage />;
    }
  })();

  return (
    <>
      <h1 className="sr-only">{PAGE_HEADINGS[page]}</h1>
      {content}
    </>
  );
};

export default App;
