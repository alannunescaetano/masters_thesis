using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using SurveyApp.Entity;

namespace SurveyApp.Controllers
{
    public class AnswersController : Controller
    {
        private readonly SurveyAppContext _context;
        private readonly string SessionKeyRespondidos = "SessionKeyRespondidos";

        public AnswersController(SurveyAppContext context)
        {
            _context = context;
        }

        public IActionResult Create()
        {
            if (string.IsNullOrEmpty(HttpContext.Session.GetString(SessionKeyRespondidos)))
                HttpContext.Session.SetString(SessionKeyRespondidos, "");

            var respondidos = HttpContext.Session.GetString(SessionKeyRespondidos).Split(";");

            var routes = _context.Routes.AsNoTracking().Where(r => !respondidos.Contains(r.Id.ToString()));
            var count = routes.Count();

            Random random = new Random();
            int n = random.Next(0, count);

            var route = routes.Skip(n).FirstOrDefault();

            if (route == null)
            {
                return RedirectToAction("End", "Answers");
            }
            else
            {
                ViewBag.ImageUrl = route.ImageUrl;
                ViewBag.RouteId = route.Id;

                return View();
            }
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,RouteId,CyclePathExists,StreetType,PavementType,PavementDefectExists,CyclistPerception,ImageUrl")] Answer answer)
        {
            if (ModelState.IsValid)
            {
                _context.Add(answer);
                await _context.SaveChangesAsync();

                string respondidos = HttpContext.Session.GetString(SessionKeyRespondidos);
                respondidos = respondidos + answer.RouteId + ";";
                HttpContext.Session.SetString(SessionKeyRespondidos, respondidos);

                return RedirectToAction();
            }

            var route = _context.Routes.AsNoTracking().First(x => x.Id == answer.RouteId);
            ViewBag.ImageUrl = route.ImageUrl;
            ViewBag.RouteId = route.Id;

            return View(answer);
        }

        public IActionResult End()
        {
            return View();
        }
    }
}
