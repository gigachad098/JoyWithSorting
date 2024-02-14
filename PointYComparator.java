import java.util.Comparator;

public class PointYComparator implements Comparator<Point> {
    @Override
    public int compare(Point firstPoint, Point secondPoint) {
        return Double.compare(firstPoint.y, secondPoint.y);
    }
}
